import React, { useState } from 'react';
import { Volunteer, Skill, Priority, ExperienceLevel, Task } from '../types';
import { X } from 'lucide-react';

const SKILLS: Skill[] = ['Medical', 'Technical', 'Logistics', 'Education', 'Legal', 'Admin'];

export function VolunteerForm({ onSubmit, onClose }: { onSubmit: (v: any) => void, onClose: () => void }) {
  const [formData, setFormData] = useState({
    name: '',
    skills: [] as Skill[],
    availability: 'Full-time' as const,
    location: '',
    experience: 'Beginner' as ExperienceLevel
  });

  return (
    <div className="bg-white p-8 rounded-2xl w-full max-w-md relative shadow-2xl">
      <button onClick={onClose} className="absolute right-4 top-4 text-gray-400 hover:text-gray-600">
        <X size={20} />
      </button>
      <h3 className="text-xl font-bold mb-6">Register Volunteer</h3>
      <form onSubmit={(e) => { e.preventDefault(); onSubmit(formData); onClose(); }} className="space-y-4">
        <div>
          <label className="block text-xs font-bold text-gray-400 uppercase mb-1">Full Name</label>
          <input required className="w-full p-3 bg-gray-50 border border-gray-100 rounded-lg outline-none focus:border-indigo-500 transition-colors" 
                 value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} />
        </div>
        <div>
          <label className="block text-xs font-bold text-gray-400 uppercase mb-1">Primary Skills</label>
          <div className="flex flex-wrap gap-2">
            {SKILLS.map(s => (
              <button key={s} type="button" 
                      onClick={() => setFormData(prev => ({
                        ...prev, 
                        skills: prev.skills.includes(s) ? prev.skills.filter(x => x !== s) : [...prev.skills, s]
                      }))}
                      className={`px-3 py-1 rounded-full text-xs font-medium transition-colors ${formData.skills.includes(s) ? 'bg-indigo-600 text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'}`}>
                {s}
              </button>
            ))}
          </div>
        </div>
        <button className="w-full py-4 bg-indigo-600 text-white rounded-xl font-bold shadow-lg shadow-indigo-200 hover:bg-indigo-700 transition-all">Register</button>
      </form>
    </div>
  );
}

export function TaskForm({ onSubmit, onClose }: { onSubmit: (t: any) => void, onClose: () => void }) {
  const [formData, setFormData] = useState({
    name: '',
    requiredSkill: 'Medical' as Skill,
    priority: 'Medium' as Priority,
    location: '',
    volunteersRequired: 1
  });

  return (
    <div className="bg-white p-8 rounded-2xl w-full max-w-md relative shadow-2xl">
      <button onClick={onClose} className="absolute right-4 top-4 text-gray-400 hover:text-gray-600">
        <X size={20} />
      </button>
      <h3 className="text-xl font-bold mb-6">Create New Task</h3>
      <form onSubmit={(e) => { e.preventDefault(); onSubmit(formData); onClose(); }} className="space-y-4">
        <div>
          <label className="block text-xs font-bold text-gray-400 uppercase mb-1">Task Name</label>
          <input required className="w-full p-3 bg-gray-50 border border-gray-100 rounded-lg outline-none focus:border-indigo-500 transition-colors" 
                 value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} />
        </div>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-xs font-bold text-gray-400 uppercase mb-1">Category</label>
            <select className="w-full p-3 bg-gray-50 border border-gray-100 rounded-lg outline-none" value={formData.requiredSkill} onChange={e => setFormData({...formData, requiredSkill: e.target.value as Skill})}>
              {SKILLS.map(s => <option key={s} value={s}>{s}</option>)}
            </select>
          </div>
          <div>
            <label className="block text-xs font-bold text-gray-400 uppercase mb-1">Volunteers Needed</label>
            <input type="number" min="1" className="w-full p-3 bg-gray-50 border border-gray-100 rounded-lg outline-none" value={formData.volunteersRequired} onChange={e => setFormData({...formData, volunteersRequired: parseInt(e.target.value)})} />
          </div>
        </div>
        <button className="w-full py-4 bg-indigo-600 text-white rounded-xl font-bold shadow-lg shadow-indigo-200 hover:bg-indigo-700 transition-all">Launch Task</button>
      </form>
    </div>
  );
}
