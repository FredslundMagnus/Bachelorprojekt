
# Parameters

    Name :                      MagicalLights2_convert4_TEST-1
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
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      68612831742 function calls (68310687559 primitive calls) in 86108.56 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86108.561 86108.561 {built-in method builtins.exec}
                      1    4.194    4.194 86108.561 86108.561 <string>:1(<module>)
                      1  349.129  349.129 86104.368 86104.368 main.py:79(CFagent)
                9798453   37.190    0.000 30735.415    0.003 agent.py:29(learn)
                9798452  761.349    0.000 25670.819    0.003 learner.py:42(Qlearn)
                3266151   14.034    0.000 19407.076    0.006 game.py:41(step)
                3266151   19.947    0.000 18591.071    0.006 layers.py:718(step)
        338208202/36065710 1446.498    0.000 13093.534    0.000 module.py:866(_call_impl)
               26267258   76.382    0.000 12278.488    0.000 network.py:27(forward)
                3266151  298.636    0.000 12240.136    0.004 layers.py:17(step)
               26267258  385.304    0.000 12035.682    0.000 container.py:117(forward)
              325572226  928.051    0.000 11910.456    0.000 layer.py:98(move)
                3266151  336.880    0.000 11853.354    0.004 agent.py:54(_learn)
                3266151  332.836    0.000 10986.378    0.003 agent.py:204(_learn)
                9798452   85.369    0.000 10976.690    0.001 optimizer.py:84(wrapper)
                9798452   42.251    0.000 10556.351    0.001 grad_mode.py:24(decorate_context)
                9798452  290.068    0.000 10419.080    0.001 adam.py:55(step)
                3266151  968.454    0.000 10341.763    0.003 agent.py:212(counterfact)
                9798452 2148.636    0.000 9805.537    0.001 _functional.py:53(adam)
                3266151  101.481    0.000 7837.333    0.002 agent.py:117(_learn)
              325572226 1527.380    0.000 7564.270    0.000 layers.py:735(check)
                3266152  468.239    0.000 6305.681    0.002 layers.py:684(update)
                9798452   42.831    0.000 6291.708    0.001 tensor.py:195(backward)
                9798452   38.097    0.000 6247.337    0.001 __init__.py:68(backward)
                8226826  220.311    0.000 6221.238    0.001 agent.py:49(__call__)
                9798452 5979.442    0.001 5979.442    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               51623450 5466.407    0.000 5466.407    0.000 {built-in method tensor}
               44101785   31.403    0.000 5242.570    0.000 game.py:37(board)
                3266151 3977.137    0.001 5070.680    0.002 replaybuffer.py:22(sample_data)
                3266151 3874.134    0.001 4937.596    0.002 replaybuffer.py:67(sample_data)
                3266151 1894.494    0.001 4349.308    0.001 agent.py:88(interveen)
               52534516  121.501    0.000 4326.633    0.000 conv.py:398(forward)
               52534516   70.758    0.000 4148.643    0.000 conv.py:390(_conv_forward)
               52534516 4077.885    0.000 4077.885    0.000 {built-in method conv2d}
               65323030 2314.713    0.000 4005.356    0.000 layer.py:151(update)
                3266151 1920.988    0.001 3678.498    0.001 replaybuffer.py:28(teleporter_save_data)
               72269472  150.337    0.000 3483.627    0.000 linear.py:93(forward)
               72269472   62.446    0.000 3257.227    0.000 functional.py:1737(linear)
               72269472 3178.843    0.000 3178.843    0.000 {built-in method torch._C._nn.linear}
                3266151 1945.011    0.001 2939.562    0.001 agent.py:67(modify)
              325572226  549.805    0.000 2798.796    0.000 layers.py:729(isFree)
                1709679   38.837    0.000 2787.144    0.002 agent.py:176(choose_action)
             2620726717 1835.532    0.000 2248.990    0.000 layer.py:95(isFree)
              182904436 2009.973    0.000 2009.973    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               98536730   81.873    0.000 1966.556    0.000 activation.py:713(forward)
               44154482 1891.908    0.000 1891.908    0.000 {built-in method cat}
               98536730   88.781    0.000 1884.682    0.000 functional.py:1364(leaky_relu)
               98536730 1777.882    0.000 1777.882    0.000 {built-in method torch._C._nn.leaky_relu}
              182904436 1770.134    0.000 1770.134    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11492977   86.911    0.000 1741.934    0.000 agent.py:59(modify_board)
              123107977 1732.280    0.000 1732.280    0.000 {built-in method clone}
                3266150   56.314    0.000 1718.517    0.001 agent.py:172(__call__)
                3266151   54.151    0.000 1595.118    0.000 agent.py:112(__call__)
             6107469887 1074.440    0.000 1538.929    0.000 enum.py:646(__hash__)
                9798452  241.557    0.000 1517.866    0.000 optimizer.py:189(zero_grad)
              326683057  333.446    0.000 1444.545    0.000 {built-in method builtins.any}
                3266151 1084.699    0.000 1409.301    0.000 replaybuffer.py:73(CF_save_data)
              325572226  906.920    0.000 1193.221    0.000 layers.py:77(check)
                3198295   41.444    0.000 1141.262    0.000 layers.py:740(restart)
             3557585955  915.772    0.000 1111.099    0.000 layers.py:700(<genexpr>)
               11492977 1100.194    0.000 1100.194    0.000 {built-in method torch._C._nn.one_hot}
               91452218 1091.226    0.000 1091.226    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              325572226  657.405    0.000 1033.944    0.000 layers.py:246(check)
              326615200  191.720    0.000  984.309    0.000 {built-in method builtins.all}
              325572226  590.734    0.000  971.943    0.000 layers.py:286(check)
               91452218  943.033    0.000  943.033    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1071604326  935.095    0.000  935.095    0.000 layer.py:146(elements)
               91452218  908.800    0.000  908.800    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               91452218  904.073    0.000  904.073    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3266151   64.799    0.000  858.583    0.000 replaybuffer.py:18(stacker)
                3266150   65.484    0.000  836.148    0.000 replaybuffer.py:63(stacker)
             2091711973  526.717    0.000  830.388    0.000 layers.py:690(<genexpr>)
                3198295   17.076    0.000  804.719    0.000 level.py:8(__init__)
             7818626168  731.148    0.000  731.148    0.000 layer.py:91(positions)
                3266151  430.025    0.000  709.949    0.000 collector.py:46(collect)
               91452218  705.887    0.000  705.887    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3198295  104.484    0.000  651.066    0.000 levels.py:199(generate)
        8683517655/8683517652  576.593    0.000  642.006    0.000 {built-in method builtins.len}
                8226826  233.841    0.000  639.902    0.000 exploration.py:53(softmaxer)
              325572226  483.547    0.000  636.778    0.000 layers.py:62(check)
              325572226  373.190    0.000  574.895    0.000 layers.py:313(check)
                1709679  478.514    0.000  567.566    0.000 agent.py:187(convert_values)
              640165610  431.372    0.000  541.264    0.000 tensor.py:906(grad)
              325572226  343.001    0.000  534.676    0.000 layers.py:273(check)
                9798452   14.241    0.000  500.922    0.000 loss.py:527(forward)
               12928892  190.190    0.000  499.782    0.000 random.py:315(sample)
                9798452   37.080    0.000  486.681    0.000 functional.py:2898(mse_loss)
             6107507102  464.496    0.000  464.496    0.000 {built-in method builtins.hash}
              137867104  456.605    0.000  456.605    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                6396590   51.425    0.000  443.593    0.000 level.py:41(notUsed)
              325572226  289.461    0.000  429.406    0.000 layers.py:48(check)
              325572226  240.121    0.000  347.881    0.000 layers.py:23(check)
                9798452  325.501    0.000  325.501    0.000 {built-in method torch._C._nn.mse_loss}
               52534516   37.461    0.000  316.487    0.000 flatten.py:39(forward)
               19596906  299.654    0.000  299.654    0.000 {built-in method sum}
                6532304  286.449    0.000  286.449    0.000 {built-in method nonzero}
               31982950   41.861    0.000  284.717    0.000 layer.py:69(restart)
                9799600  283.808    0.000  283.808    0.000 {built-in method max}
             3595198396  282.885    0.000  282.885    0.000 {method 'random' of '_random.Random' objects}
              278841149  207.517    0.000  281.697    0.000 layer.py:126(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9572854: <MagicalLights2_convert4_TEST_1> in cluster <dcc> Done

Job <MagicalLights2_convert4_TEST_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 26 00:55:52 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 26 01:11:38 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 26 01:11:38 2021
Terminated at Tue Apr 27 01:06:53 2021
Results reported at Tue Apr 27 01:06:53 2021

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

    CPU time :                                   85895.48 sec.
    Max Memory :                                 9445 MB
    Average Memory :                             6252.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6939.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            87061 sec.

The output (if any) is above this job summary.

