
# Parameters

    Name :                      ReTest10-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              1
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      65294926290 function calls (65058931443 primitive calls) in 86119.90 seconds

##    Ordered by: cumulative time
   List reduced from 504 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86119.896 86119.896 {built-in method builtins.exec}
                      1    3.740    3.740 86119.896 86119.896 <string>:1(<module>)
                      1  311.859  311.859 86116.156 86116.156 main.py:75(CFagent)
                8838087   33.905    0.000 34162.598    0.004 agent.py:29(learn)
                8834448  774.788    0.000 28847.468    0.003 learner.py:42(Qlearn)
                2946029   14.412    0.000 19130.319    0.006 game.py:41(step)
                2946029   18.763    0.000 18329.962    0.006 layers.py:718(step)
                2946029  106.847    0.000 13156.061    0.004 agent.py:54(_learn)
                8834448   55.065    0.000 12458.999    0.001 grad_mode.py:23(decorate_context)
                8834448  324.932    0.000 12298.722    0.001 adam.py:55(step)
                2946029  277.884    0.000 12280.713    0.004 layers.py:17(step)
                2946029  107.826    0.000 12246.010    0.004 agent.py:202(_learn)
        265475710/29482554 1129.291    0.000 12199.272    0.000 module.py:715(_call_impl)
              294100530  881.041    0.000 11976.028    0.000 layer.py:98(move)
               20648106   55.516    0.000 11423.961    0.001 network.py:24(forward)
               20648106  288.935    0.000 11239.601    0.001 container.py:115(forward)
                8834448 2266.282    0.000 10605.659    0.001 functional.py:53(adam)
                2946029   85.961    0.000 8706.980    0.003 agent.py:117(_learn)
              294100530 1399.972    0.000 7373.235    0.000 layers.py:735(check)
                8834448   55.015    0.000 6571.887    0.001 tensor.py:181(backward)
                2946029  669.584    0.000 6516.875    0.002 agent.py:210(counterfact)
                8834448   31.710    0.000 6516.871    0.001 __init__.py:68(backward)
                8834448 6241.589    0.001 6241.589    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2946030  463.468    0.000 6004.838    0.002 layers.py:684(update)
                5903240  149.693    0.000 5250.682    0.001 agent.py:49(__call__)
               44392262 4894.976    0.000 4894.976    0.000 {built-in method tensor}
                2946029 3387.681    0.001 4856.310    0.002 replaybuffer.py:22(sample_data)
                2946029 2133.726    0.001 4750.033    0.002 agent.py:88(interveen)
               37574247   25.158    0.000 4651.578    0.000 game.py:37(board)
                2946029 2840.371    0.001 4282.349    0.001 replaybuffer.py:52(sample_data)
               41296212   84.051    0.000 4016.572    0.000 conv.py:422(forward)
                2946029 2024.835    0.001 4007.100    0.001 replaybuffer.py:28(teleporter_save_data)
               41296212   82.931    0.000 3901.528    0.000 conv.py:414(_conv_forward)
               41296212 3799.927    0.000 3799.927    0.000 {built-in method conv2d}
               58920590 2107.272    0.000 3703.433    0.000 layer.py:151(update)
               56052260  142.218    0.000 3689.317    0.000 linear.py:92(forward)
               56052260  225.251    0.000 3480.906    0.000 functional.py:1669(linear)
                2946029 1749.888    0.001 3398.714    0.001 agent.py:67(modify)
              294100530  626.698    0.000 3123.078    0.000 layers.py:729(isFree)
               38291364 2642.173    0.000 2642.173    0.000 {built-in method cat}
              577167038 1646.862    0.000 2586.676    0.000 tensor.py:933(grad)
                8834448  232.977    0.000 2510.847    0.000 optimizer.py:167(zero_grad)
             2763527478 2042.531    0.000 2496.379    0.000 layer.py:95(isFree)
               56052260 2483.096    0.000 2483.096    0.000 {built-in method addmm}
              164904844 2244.486    0.000 2244.486    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1114245455  652.986    0.000 2203.427    0.000 {built-in method builtins.any}
              164904844 1882.490    0.000 1882.490    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2942390   49.621    0.000 1823.437    0.001 agent.py:171(__call__)
              110845348 1787.386    0.000 1787.386    0.000 {built-in method clone}
                2946029   50.254    0.000 1687.674    0.001 agent.py:112(__call__)
               76700366   67.894    0.000 1687.585    0.000 activation.py:713(forward)
               76700366  101.614    0.000 1619.691    0.000 functional.py:1292(leaky_relu)
                8849269   66.314    0.000 1560.248    0.000 agent.py:59(modify_board)
             5660811286 1075.807    0.000 1527.469    0.000 enum.py:646(__hash__)
               76700366 1507.867    0.000 1507.867    0.000 {built-in method torch._C._nn.leaky_relu}
                2946029  862.598    0.000 1349.349    0.000 replaybuffer.py:58(CF_save_data)
               29502749  171.802    0.000 1290.187    0.000 tensor.py:21(wrapped)
              745174019  425.698    0.000 1254.423    0.000 overrides.py:1070(has_torch_function)
                2946029   57.814    0.000 1246.989    0.000 replaybuffer.py:18(stacker)
                2942390   55.303    0.000 1226.204    0.000 replaybuffer.py:48(stacker)
               82452422 1195.619    0.000 1195.619    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              324105749  164.068    0.000 1178.548    0.000 {built-in method builtins.all}
              294100530  889.506    0.000 1174.387    0.000 layers.py:77(check)
               82452422 1098.569    0.000 1098.569    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             3216446750  889.450    0.000 1086.791    0.000 layers.py:700(<genexpr>)
              294100530  675.549    0.000 1049.197    0.000 layers.py:246(check)
             1492705902  409.126    0.000 1032.092    0.000 layers.py:690(<genexpr>)
               82452422  991.883    0.000  991.883    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8849269  978.668    0.000  978.668    0.000 {built-in method torch._C._nn.one_hot}
              294100530  600.209    0.000  971.413    0.000 layers.py:286(check)
               82452422  898.663    0.000  898.663    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              885592559  882.519    0.000  882.519    0.000 layer.py:146(elements)
                2198750   29.767    0.000  860.595    0.000 layers.py:740(restart)
                2946029  459.789    0.000  767.608    0.000 collector.py:46(collect)
             7617064766  747.525    0.000  747.525    0.000 layer.py:91(positions)
               82452422  699.229    0.000  699.229    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              294100530  509.552    0.000  653.295    0.000 layers.py:62(check)
                2198750   13.474    0.000  610.535    0.000 level.py:8(__init__)
        7106216901/7106216898  481.609    0.000  599.825    0.000 {built-in method builtins.len}
              122637007  585.412    0.000  585.412    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                5903240  197.882    0.000  564.364    0.000 exploration.py:53(softmaxer)
              294603000  372.891    0.000  556.824    0.000 layers.py:113(isDone)
              294100530  358.248    0.000  546.566    0.000 layers.py:273(check)
                8834448   14.553    0.000  533.098    0.000 loss.py:445(forward)
                2946029   98.557    0.000  525.999    0.000 agent.py:277(counterfact_check)
                8834448   48.784    0.000  518.544    0.000 functional.py:2637(mse_loss)
               56052260  508.745    0.000  508.745    0.000 {method 't' of 'torch._C._TensorBase' objects}
              294100530  324.187    0.000  505.519    0.000 layers.py:313(check)
               20622203  497.539    0.000  497.539    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                2198750   81.664    0.000  484.868    0.000 levels.py:199(generate)
               10289558  174.000    0.000  463.605    0.000 random.py:315(sample)
             1575902457  367.388    0.000  457.885    0.000 overrides.py:1083(<genexpr>)
             5660844917  451.669    0.000  451.669    0.000 {built-in method builtins.hash}
              294100530  287.754    0.000  422.855    0.000 layers.py:48(check)
                5889599  399.302    0.000  399.302    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               20622203  356.535    0.000  356.535    0.000 {built-in method sum}
              294100530  233.212    0.000  344.438    0.000 layers.py:23(check)
                4397500   38.996    0.000  327.900    0.000 level.py:41(notUsed)
                8834448  327.661    0.000  327.661    0.000 {built-in method torch._C._nn.mse_loss}
               41296212   29.934    0.000  305.052    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9515001: <ReTest10_0> in cluster <dcc> Done

Job <ReTest10_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Wed Apr 14 13:56:06 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 15 10:52:21 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 15 10:52:21 2021
Terminated at Fri Apr 16 10:47:49 2021
Results reported at Fri Apr 16 10:47:49 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
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

    CPU time :                                   85899.48 sec.
    Max Memory :                                 3295 MB
    Average Memory :                             3229.94 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13089.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86178 sec.
    Turnaround time :                            161503 sec.

The output (if any) is above this job summary.

