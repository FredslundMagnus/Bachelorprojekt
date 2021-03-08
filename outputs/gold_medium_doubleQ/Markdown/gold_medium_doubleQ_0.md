/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [0,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [1,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [2,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [3,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [4,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [5,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [6,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [7,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
THCudaCheck FAIL file=/pytorch/torch/csrc/generic/serialization.cpp line=31 error=710 : device-side assert triggered
Traceback (most recent call last):
  File "main.py", line 28, in teleport
    teleporter.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 28, in learn
    self._learn(state_after, action, reward, done, *args)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 52, in _learn
    self.learner.learn(self.values, state_after, action, reward, done)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/learner.py", line 37, in DoubleQlearn
    loss_value_network = self.criterion(action_value_before, td_target)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/nn/modules/module.py", line 889, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/nn/modules/loss.py", line 528, in forward
    return F.mse_loss(input, target, reduction=self.reduction)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/nn/functional.py", line 2926, in mse_loss
    return torch._C._nn.mse_loss(expanded_input, expanded_target, _Reduction.get_enum(reduction))
RuntimeError: CUDA error: device-side assert triggered

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "main.py", line 29, in teleport
    collector.collect([rewards, modified_rewards, teleport_rewards], [dones, modified_dones])
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 16, in __exit__
    self.save()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 21, in save
    self.saveObject(element, start, element.__class__.__name__)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 26, in saveObject
    pickle.dump(element, open(Save.path(start, _class) + name, "wb"))
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/storage.py", line 54, in __reduce__
    torch.save(self, b, _use_new_zipfile_serialization=False)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/serialization.py", line 374, in save
    _legacy_save(obj, opened_file, pickle_module, pickle_protocol)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/serialization.py", line 447, in _legacy_save
    serialized_storages[key]._write_file(f, _should_read_directly(f), True)
RuntimeError: cuda runtime error (710) : device-side assert triggered at /pytorch/torch/csrc/generic/serialization.cpp:31


# Parameters

    Name :                      gold_medium_doubleQ-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.DoubleQlearn
    Learner2 :                  Learners.DoubleQlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      138907 function calls (138606 primitive calls) in 12.62 seconds

##    Ordered by: cumulative time
   List reduced from 391 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   12.621   12.621 {built-in method builtins.exec}
                      1    0.000    0.000   12.621   12.621 <string>:1(<module>)
                      1    0.000    0.000   12.621   12.621 main.py:10(teleport)
                      2    0.000    0.000   12.152    6.076 agent.py:14(__init__)
                      2    0.000    0.000   12.151    6.075 network.py:33(__init__)
                      1    0.000    0.000   12.143   12.143 agent.py:93(__init__)
                      6    0.000    0.000   12.105    2.017 module.py:573(to)
                   72/6    0.001    0.000   12.105    2.017 module.py:385(_apply)
                     54    0.000    0.000   12.103    0.224 module.py:667(convert)
                     55   12.102    0.220   12.103    0.220 {method 'to' of 'torch._C._TensorBase' objects}
                      2    0.000    0.000    0.200    0.100 agent.py:26(learn)
                      2    0.000    0.000    0.199    0.099 learner.py:30(DoubleQlearn)
                   87/9    0.000    0.000    0.196    0.022 module.py:866(_call_impl)
                      1    0.000    0.000    0.149    0.149 agent.py:50(_learn)
                      2    0.000    0.000    0.147    0.074 loss.py:527(forward)
                      2    0.000    0.000    0.147    0.074 functional.py:2898(mse_loss)
                      2    0.126    0.063    0.126    0.063 {built-in method torch._C._nn.mse_loss}
                      1    0.008    0.008    0.111    0.111 agent.py:77(interveen)
                      2    0.000    0.000    0.103    0.052 agent.py:45(__call__)
                      1    0.000    0.000    0.051    0.051 agent.py:101(_learn)
                      1    0.000    0.000    0.049    0.049 game.py:8(__init__)
                      7    0.000    0.000    0.049    0.007 network.py:24(forward)
                      7    0.000    0.000    0.049    0.007 container.py:117(forward)
                      6    0.000    0.000    0.046    0.008 network.py:15(__init__)
                      2    0.000    0.000    0.044    0.022 layers.py:192(update)
                      1    0.000    0.000    0.042    0.042 agent.py:88(pre_process)
                     12    0.000    0.000    0.040    0.003 conv.py:370(__init__)
                     12    0.008    0.001    0.040    0.003 conv.py:66(__init__)
                    100    0.001    0.000    0.039    0.000 layers.py:233(restart)
                     27    0.000    0.000    0.033    0.001 init.py:347(kaiming_uniform_)
                    100    0.000    0.000    0.032    0.000 levels.py:8(__init__)
                      1    0.031    0.031    0.031    0.031 agent.py:59(modify)
                    100    0.000    0.000    0.031    0.000 level.py:8(__init__)
                     54    0.031    0.001    0.031    0.001 {method 'uniform_' of 'torch._C._TensorBase' objects}
                    100    0.005    0.000    0.030    0.000 levels.py:11(generate)
                     12    0.000    0.000    0.030    0.003 conv.py:114(reset_parameters)
                      2    0.020    0.010    0.030    0.015 exploration.py:53(softmaxer)
                      1    0.000    0.000    0.029    0.029 tensor.py:195(backward)
                      1    0.000    0.000    0.029    0.029 __init__.py:68(backward)
                      1    0.029    0.029    0.029    0.029 {method 'run_backward' of 'torch._C._EngineBase' objects}
                      2    0.028    0.014    0.028    0.014 {built-in method nonzero}
                      3    0.000    0.000    0.028    0.009 agent.py:54(modify_board)
                      3    0.027    0.009    0.027    0.009 {built-in method torch._C._nn.one_hot}
                      1    0.000    0.000    0.026    0.026 save.py:15(__exit__)
                      1    0.000    0.000    0.026    0.026 save.py:18(save)
                      2    0.021    0.011    0.021    0.011 functional.py:46(broadcast_tensors)
                      1    0.000    0.000    0.019    0.019 optimizer.py:84(wrapper)
                      1    0.000    0.000    0.019    0.019 grad_mode.py:24(decorate_context)
                      1    0.000    0.000    0.019    0.019 adam.py:55(step)
                      3    0.004    0.001    0.019    0.006 save.py:24(saveObject)
                      1    0.000    0.000    0.018    0.018 _functional.py:53(adam)
                      8    0.017    0.002    0.017    0.002 {method 'sqrt' of 'torch._C._TensorBase' objects}
                     14    0.000    0.000    0.017    0.001 conv.py:398(forward)
                     14    0.000    0.000    0.017    0.001 conv.py:390(_conv_forward)
                     14    0.017    0.001    0.017    0.001 {built-in method conv2d}
                     25    0.000    0.000    0.017    0.001 activation.py:713(forward)
                     25    0.000    0.000    0.017    0.001 functional.py:1364(leaky_relu)
                     25    0.016    0.001    0.016    0.001 {built-in method torch._C._nn.leaky_relu}
                     18    0.000    0.000    0.014    0.001 linear.py:93(forward)
                     18    0.000    0.000    0.014    0.001 functional.py:1737(linear)
                     18    0.014    0.001    0.014    0.001 {built-in method torch._C._nn.linear}
                    100    0.007    0.000    0.013    0.000 levels.py:76(RFS)
                      1    0.000    0.000    0.012    0.012 agent.py:36(__init__)
                      4    0.000    0.000    0.011    0.003 save.py:28(path)
                      4    0.011    0.003    0.011    0.003 {built-in method flatten}
                    200    0.005    0.000    0.010    0.000 layers.py:37(reset)
                      2    0.010    0.005    0.010    0.005 {built-in method multinomial}
                      8    0.000    0.000    0.008    0.001 genericpath.py:16(exists)
                      8    0.008    0.001    0.008    0.001 {built-in method posix.stat}
                    400    0.001    0.000    0.007    0.000 layer.py:40(restart)
                      1    0.000    0.000    0.006    0.006 layers.py:147(__init__)
                    7/3    0.002    0.000    0.006    0.002 {built-in method _pickle.dump}
                      4    0.000    0.000    0.006    0.001 layer.py:26(__init__)
                      3    0.005    0.002    0.005    0.002 {built-in method io.open}
                     15    0.000    0.000    0.004    0.000 linear.py:75(__init__)
                    100    0.001    0.000    0.004    0.000 level.py:34(notUsed)
                   8777    0.003    0.000    0.004    0.000 layer.py:76(add)
                      4    0.004    0.001    0.004    0.001 {built-in method zeros}
                      1    0.000    0.000    0.004    0.004 storage.py:52(__reduce__)
                      1    0.000    0.000    0.004    0.004 serialization.py:333(save)
                      1    0.000    0.000    0.004    0.004 serialization.py:377(_legacy_save)
                      1    0.004    0.004    0.004    0.004 {method '_write_file' of 'torch._C.CudaFloatStorageBase' objects}
                   4900    0.003    0.000    0.003    0.000 level.py:25(inverse)
                      3    0.003    0.001    0.003    0.001 {built-in method posix.mkdir}
                      8    0.002    0.000    0.003    0.000 layer.py:90(update)
                     15    0.000    0.000    0.003    0.000 linear.py:86(reset_parameters)
                   6000    0.002    0.000    0.003    0.000 levels.py:33(<genexpr>)
                      4    0.002    0.001    0.002    0.001 {method 'long' of 'torch._C._TensorBase' objects}
                   1104    0.002    0.000    0.002    0.000 module.py:950(__setattr__)
                  16728    0.002    0.000    0.002    0.000 layer.py:100(grid)
                   1600    0.001    0.000    0.002    0.000 random.py:285(choice)
                     74    0.000    0.000    0.002    0.000 module.py:250(__init__)
                      1    0.000    0.000    0.002    0.002 game.py:21(step)
                     54    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                      1    0.000    0.000    0.002    0.002 layers.py:212(step)
                     27    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                   6004    0.001    0.000    0.002    0.000 enum.py:646(__hash__)
                   2113    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
                  21602    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                    201    0.001    0.000    0.001    0.000 random.py:315(sample)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9393242: <gold_medium_doubleQ_0> in cluster <dcc> Done

Job <gold_medium_doubleQ_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 01:58:30 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 01:58:35 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 01:58:35 2021
Terminated at Mon Mar  8 01:59:07 2021
Results reported at Mon Mar  8 01:59:07 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   4.77 sec.
    Max Memory :                                 110 MB
    Average Memory :                             110.00 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               8082.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   36 sec.
    Turnaround time :                            37 sec.

The output (if any) is above this job summary.

